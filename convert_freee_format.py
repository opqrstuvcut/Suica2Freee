#! /usr/bin/env python3
import argparse
import numpy as np
import pandas as pd
import datetime
import re
from collections import defaultdict
from chardet.universaldetector import UniversalDetector


def parse_argument():
    parser = argparse.ArgumentParser("", add_help=True)
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    return args


def detect_encode(path):
    detector = UniversalDetector()
    with open(path, "rb") as f:
        for row in f:
            detector.reset()
            detector.feed(row)
            if detector.done:
                break

    detector.close()
    return detector.result


def main():
    args = parse_argument()
    df_dict = defaultdict(list)

    encode = detect_encode(args.input)
    date_reg = r"[0-9]{4}\/\d{1,2}\/\d{1,2}"
    year = str(datetime.datetime.now().year)

    with open(args.input, "r", encoding=encode["encoding"]) as f:
        with open(args.output, "w") as g:
            g.write(",".join(["発生日", "勘定科目", "金額", "決済口座", "備考\n"]))

            for row in f:
                split_row = row.strip().split("\t")
                if len(split_row) == 7:
                    date, type1, s, type2, e, res, payment = split_row
                else:
                    continue

                if type1 != "入":
                    continue

                if not re.match(date_reg, date):
                    date = year + "/" + date
                df_dict["発生日"].append(date)
                df_dict["勘定科目"].append("旅費交通費")
                df_dict["金額"].append(
                    str(np.abs(int(payment.replace('"', "").replace(",", "")))))
                df_dict["決済口座"].append("現金")
                df_dict["備考"].append(s+"から"+e)

    df = pd.DataFrame(df_dict)
    df["発生日"] = pd.to_datetime(df["発生日"], format='%Y/%m/%d')
    df.to_excel(args.output, index=False)


if __name__ == '__main__':
    main()
