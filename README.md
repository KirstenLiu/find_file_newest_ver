# find_file_newest_ver
In a givern folder (can be nested), find the file with given filename format including date format inside and date, and find the newest version of that filename. Can also be a filename without version (handled by last_idx_chop var, which chopped the tail of anything include and after v#.)

This is designed for daily ingest. Backfill can be perform with looping over time range.

Wrap as lib to use as one of the toolkit, and provide launch.json for vscode.
/docs and /tests not provided because of corperate data.
