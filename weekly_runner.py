from agents.batch_agent import BatchAnalysisAgent

from reports.weekly_report import create_weekly_report

from tools.email_sender import send_email



def run_weekly():


    agent=BatchAnalysisAgent()


    results=agent.run()


    report=create_weekly_report(
        results
    )


    send_email(
        report
    )



if __name__=="__main__":

    run_weekly()