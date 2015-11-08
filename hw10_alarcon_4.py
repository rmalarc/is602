
import pandas as pd
import matplotlib.pyplot as plt

# Author: Mauricio Alarcon <rmalarc@msn.com>

if __name__ == "__main__":

    epa_http_data = pd.read_csv('epa-http.txt',sep=' ', error_bad_lines=False)
    epa_http_data.columns = ['requester','time','request','http_status','size']

    ## DO SOME CLEAN-UP

    # clean up size.... turn '-' into zeros
    epa_http_data.size = epa_http_data[['size']].convert_objects(convert_numeric=True)

    # extract hour
    epa_http_data['hour'] =  epa_http_data.time.str.split(':').str[1]
    epa_http_data['hour'] = epa_http_data['hour'].convert_objects(convert_numeric=True)
    epa_http_data['hour'] = epa_http_data['hour'].apply(lambda x: "%02d-%02d"%(x.astype('int'),x.astype('int')+1))

    # extract the filename

    # try those requests that start with GET,POST,HEAD ... REQUEST .... HTTP/1.0
    epa_http_data['filename'] = \
        epa_http_data.request.str.extract('(GET|POST|HEAD) (.+) HTTP.*')[1]

    # try those requests that start with GET,POST,HEAD ... REQUEST
    epa_http_data.loc[epa_http_data.filename.isnull(),['filename']] = \
        epa_http_data.request.str.extract('(GET|POST|HEAD) (.+)')[1]

    # Fill the remaining with the request
    epa_http_data['filename'] = \
        epa_http_data['filename'].fillna(epa_http_data.request)


    # Which hostname or IP address made the most requests?
    print "---------------"
    print "Which hostname or IP address made the most requests?"
    print epa_http_data.requester.value_counts().head(1)

    # Which hostname or IP address received the most total bytes from the server? How many bytes did it receive?
    print "---------------"
    print "Which hostname or IP address received the most total bytes from the server? How many bytes did it receive?"
    print epa_http_data.loc[:,['requester','size']].groupby('requester').sum().sort_values(by='size', ascending=False).head(1)

    # During what hour was the server the busiest in terms of requests?
    print "---------------"
    print "During what hour was the server the busiest in terms of requests?"
    traffic_by_hour = epa_http_data.loc[:,['hour','request']].groupby('hour').count()
    print traffic_by_hour
    busiest_hour = traffic_by_hour.sort_values(by='request',ascending=False).head(1)
    print "As we can see above, the time between %s is the busiest with a total of %i requests in the date range" \
          %(busiest_hour.index[0],busiest_hour.request)

    # Which .gif image was downloaded the most during the day?
    print "---------------"
    print "Which .gif image was downloaded the most during the day?"
    print epa_http_data.loc[epa_http_data.filename.str.endswith('gif'),['filename','request']]\
        .groupby('filename').count()\
        .sort_values(by='request',ascending=False).head(1)

    # What HTTP reply codes were sent other than 200?
    print "---------------"
    print "What HTTP reply codes were sent other than 200?"
    print epa_http_data.loc[epa_http_data.http_status != 200,['http_status','request']]\
        .groupby('http_status').count()\
        .sort_values(by='request',ascending=False)


    print traffic_by_hour.columns.values
    plt.plot(traffic_by_hour['request'])
    plt.xticks(range(len(traffic_by_hour.index)), traffic_by_hour.index,rotation=70)
    plt.title('EPA Website Traffic by Time of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Traffic')
    plt.grid(True)
    plt.show()
