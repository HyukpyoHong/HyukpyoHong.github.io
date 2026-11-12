import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('sync', Path(__file__).resolve().parents[1] / 'sync_from_sheets.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class DisplayOrderTests(unittest.TestCase):
    def test_papers_append_order_and_source_unchanged(self):
        rows = [{'title': 'older'}, {'title': 'newer'}]
        self.assertEqual([r['title'] for r in sync.newest_first('papers', rows)], ['newer', 'older'])
        self.assertEqual(rows[0]['title'], 'older')

    def test_talk_dates_not_row_order(self):
        rows = [{'date': d} for d in ['y2026-12-22y', 'y2026-11-05y', 'y2026-11-16y']]
        self.assertEqual([r['date'] for r in sync.newest_first('talks', rows)],
                         ['y2026-12-22y', 'y2026-11-16y', 'y2026-11-05y'])

    def test_terms_ranges_and_stable_ties(self):
        self.assertGreater(sync.date_key('Fall 2025'), sync.date_key('Spring 2025'))
        self.assertGreater(sync.date_key('Jun. 2024 – present'), sync.date_key('Jun. 2023 – Mar. 2025'))
        self.assertEqual(sync.date_key('2019–2023'), (2019, 0, 0))
        rows = [{'year': '2025', 'title': 'a'}, {'year': '2025', 'title': 'b'}]
        self.assertEqual(sync.newest_first('awards', rows), rows)

    def test_visibility_flags_and_private_scratch_rows(self):
        rows = [dict(cv='false', web='false'),
                dict(period='2026', name='CV only', description='Research', institution='KIAS', cv='true', web='false')]
        with patch.object(sync, 'fetch_sheet', return_value=rows):
            result = sync.validated_sheet('teaching_mentoring')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['web'], 'FALSE')
        self.assertEqual(result[0]['cv'], 'TRUE')

    def test_invalid_visible_row_still_rejected(self):
        with patch.object(sync, 'fetch_sheet', return_value=[{'name': 'Incomplete', 'web': 'TRUE'}]):
            with self.assertRaisesRegex(RuntimeError, 'missing required'):
                sync.validated_sheet('teaching_mentoring')

    def test_explicit_header_row(self):
        import io
        with patch.object(sync.urllib.request, 'urlopen', return_value=io.BytesIO(b'name,cv\nExample,TRUE\n')) as request:
            self.assertEqual(sync.fetch_sheet('teaching_mentoring')[0]['name'], 'Example')
        self.assertIn('headers=1', request.call_args.args[0])


if __name__ == '__main__':
    unittest.main()
