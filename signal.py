from datetime import datetime # this is for displaying the date how we want it
import pandas as pd # this is for loading the file and writing the new ones

# load the file
df = pd.read_csv('messages.csv')

# this makes the contacts into a list
contacts = df['conversationId'].unique()

# for each contact, do the following:
for contact in contacts:
    
    # loads just the messages from contact
    messages = df[df['conversationId']==contact]

    # converts 'sent_at' and 'received_at' into a readable date format
    for index, row in messages.iterrows():
        messages['sent_at'][index] = str(datetime.fromtimestamp(int(str(messages['sent_at'][index])[0:10])))
        messages['received_at'][index] = str(datetime.fromtimestamp(int(str(messages['received_at'][index])[0:10])))

    # saves the messages to a new csv file
    messages.to_csv(f'{contact}.csv', index=False)
    
    # removes processed messages from program to make it run a little less slow
    df = df[df['conversationId']!=contact]
