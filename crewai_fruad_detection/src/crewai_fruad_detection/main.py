from crewai_fruad_detection.crew import CrewaiFruadDetection

inputs = input("Enter the topic: ")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': "Debit Card Fraud Detection"
        
    }

    try:
        CrewaiFruadDetection().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
