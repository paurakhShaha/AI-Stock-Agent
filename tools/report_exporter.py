def export_markdown(report,ticker):


    filename=f"{ticker}_report.md"


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:


        f.write(
            f"# {report['title']}\n\n"
        )


        f.write(
            report["summary"]
        )


        f.write("\n\n")


        f.write(
            "## Recommendation\n"
        )


        f.write(
            report["recommendation"]
        )



    return filename