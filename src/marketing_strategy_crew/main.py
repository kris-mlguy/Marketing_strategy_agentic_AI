#!/usr/bin/env python
import sys
import warnings
from datetime import date
from marketing_strategy_crew.crew import MarketingStrategyCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
today = date.today()

def run():
    """
    Run the crew.
    """
    inputs = {
        'org': 'Rogers',
        'overall_count': 5,
        'required_count': 2,
        'date': today.strftime("%Y-%m-%d"),    
        }
    MarketingStrategyCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MarketingStrategyCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MarketingStrategyCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'org': 'Rogers',
        'overall_count': 20,
        'required_count': 2
    }
    try:
        MarketingStrategyCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
