from flask import Flask, render_template
import meetup.api
import os
app = Flask(__name__)

@app.route('/failwhale')
def hello_world():
	strings = []
    
	client = meetup.api.Client(os.getenv('meetupkey'))

	rsvps=client.GetRsvps(event_id='235484841', urlname='_ChiPy_')
	member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
	members = client.GetMembers(member_id=member_id)

	for member in members.results:
		try:
			strings.append((member['photo']['thumb_link']))
		except:
			pass # ignore those who do not have a complete profile

	return render_template('hey.html', stuff=strings)

if __name__ == '__main__':
    app.run(debug=True)


