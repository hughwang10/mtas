from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/mtasxdms/<path:path>')
def mtasxdms(path):
  xcap_req = path.split("/")

  # example_str = """<ss:communication-diversion xmlns:ss="http://uri.etsi.org/ngn/params/xml/simservs/xcap" active="true">
  # <ss:NoReplyTimer>30</ss:NoReplyTimer>
  # <cp:ruleset xmlns:cp="urn:ietf:params:xml:ns:common-policy">
  # <cp:rule id="cfb">
  # <cp:conditions>
  # <ss:rule-deactivated/>
  # <ss:busy/>
  # </cp:conditions>
  # <cp:actions>
  # <ss:forward-to>
  # <ss:target>tel:+31621552038</ss:target>
  # </ss:forward-to>
  # </cp:actions>
  # </cp:rule>
  # <cp:rule id="cfnrc">
  # <cp:conditions>
  # <ss:not-reachable/>
  # </cp:conditions>
  # <cp:actions>
  # <ss:forward-to>
  # <ss:target>sip:+31621552038@ims.mnc004.mcc204.3gppnetwork.org;user=phone</ss:target>
  # </ss:forward-to>
  # </cp:actions>
  # </cp:rule>
  # <cp:rule id="cfnr">
  # <cp:conditions>
  # <ss:rule-deactivated/>
  # <ss:no-answer/>
  # </cp:conditions>
  # <cp:actions>
  # <ss:forward-to>
  # <ss:target>tel:+31654502100</ss:target>
  # </ss:forward-to>
  # <ss:NoReplyTimer>30</ss:NoReplyTimer>
  # </cp:actions>
  # </cp:rule>
  # <cp:rule id="cfu">
  # <cp:conditions>
  # <ss:rule-deactivated/>
  # </cp:conditions>
  # <cp:actions>
  # <ss:forward-to>
  # <ss:target>sip:+31433551208@ims.mnc004.mcc204.3gppnetwork.org;user=phone</ss:target>
  # </ss:forward-to>
  # </cp:actions>
  # </cp:rule>
  # </cp:ruleset>
  # </ss:communication-diversion>"""
  # t = 'test'


  print(request.headers)
  test_str = """<ss:communication-diversion xmlns:ss="http://uri.etsi.org/ngn/params/xml/simservs/xcap" active="true">\
  <ss:NoReplyTimer>30</ss:NoReplyTimer><cp:ruleset xmlns:cp="urn:ietf:params:xml:ns:common-policy"><cp:rule id="cfb"><cp:conditions><ss:rule-deactivated/><ss:busy/></cp:conditions><cp:actions><ss:forward-to><ss:target>tel:+31621552038</ss:target></ss:forward-to></cp:actions></cp:rule><cp:rule id="cfnrc">
  <cp:conditions>
    <ss:not-reachable/>
  </cp:conditions>
  <cp:actions>
    <ss:forward-to>
      <ss:target>sip:+31621552038@ims.mnc004.mcc204.3gppnetwork.org;user=phone</ss:target>
    </ss:forward-to>
  </cp:actions>
</cp:rule><cp:rule id="cfnr"><cp:conditions><ss:rule-deactivated/><ss:no-answer/></cp:conditions><cp:actions><ss:forward-to><ss:target>tel:+31654502100</ss:target></ss:forward-to><ss:NoReplyTimer>30</ss:NoReplyTimer></cp:actions></cp:rule><cp:rule id="cfu">
  <cp:conditions><ss:rule-deactivated/></cp:conditions>
  <cp:actions><ss:forward-to><ss:target>sip:+31433551208@ims.mnc004.mcc204.3gppnetwork.org;user=phone</ss:target></ss:forward-to></cp:actions>
</cp:rule></cp:ruleset></ss:communication-diversion>"""
  resp = make_response(test_str) # jsonify(auid=xcap_req[0],user=xcap_req[2],service=xcap_req[6])
  resp.headers['Server'] = "Apache-Coyote/1.1"
  resp.headers['X-Frame-Options'] = "DENY"
  resp.headers['X-Content-Type-Options'] = "1; mode=block"
  resp.headers['Cache-Control'] = "no-cache"
  resp.headers['ETag'] = "34"
  resp.headers['Content-Type'] = "application/xcap-el+xml"
  return resp  

    # resp.headers['Server'] = "Apache-Coyote/1.1"

# DO not modify port number here
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)