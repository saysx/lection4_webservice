import re
from typing import List
from compile_md import get_md_files

LECTION_FILE_REGEXP = r"lec4_(\d+).*?.md"


def group_report(ids: List[int], start_id: int, end_id: int, group_name: str = "unknown"):
    group_ids = list(range(start_id, end_id+1))
    done_count = len(list(filter(lambda x: x in ids, group_ids)))
    not_done_ids = list(filter(lambda x: x not in ids, group_ids))
    print(f"\nОтчет по группе {group_name}")
    print(f"Завершено {(done_count / (end_id - start_id + 1)) * 100.0}%")
    print(f"Не завершены слайды: {', '.join(str(i) for i in not_done_ids)}")


def main():
    files = get_md_files("lection/")
    matches = [re.search(LECTION_FILE_REGEXP, f.name) for f in files]
    ids = [int(m.group(1)) for m in matches if m]
    group_report(ids, 1, 34, group_name="438-1")
    group_report(ids, 35, 69, group_name="438-2")
    group_report(ids, 70, 99, group_name="438-3")    


if __name__ == "__main__":
    main()

