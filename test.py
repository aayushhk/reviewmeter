from google_play_scraper import app
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = '<YOUR ENDPOINT URL>'
api_key = '<AZURE API KEY>'

# Create a TextAnalyticsClient with your credentials
credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)




class r:
    y=input("Enter app ID: ")
    result = app(y)

    comments = result.get('comments')
    # Split comments into batches of 10 or fewer
    batch_size = 10
    positive_feedbacks = []
    negative_feedbacks = []

    for i in range(0, len(comments), batch_size):
        batch = comments[i:i+batch_size]

    # Perform sentiment analysis
        result_sentiment = text_analytics_client.analyze_sentiment(documents=batch)

    # Process the results for each comment in the batch
        for idx, doc in enumerate(result_sentiment):
            comment = batch[idx]
            if doc.sentiment == "positive":
                positive_feedbacks.append(comment)
            elif doc.sentiment == "negative":
                negative_feedbacks.append(comment)

    # Summarize the positive feedbacks
    if positive_feedbacks:
        print("Summary of Positive Feedbacks:")
        for idx, feedback in enumerate(positive_feedbacks, start=1):
            print(f"{idx}. {feedback}")
    else:
        print("No positive feedbacks found.")

    # Summarize the negative feedbacks
    if negative_feedbacks:
        print("\nSummary of Negative Feedbacks:")
        for idx, feedback in enumerate(negative_feedbacks, start=1):
           print(f"{idx}. {feedback}")
    else:
        print("\nNo negative feedbacks found.")




















