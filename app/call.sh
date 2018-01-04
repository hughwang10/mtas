### Test
ue='+31611808148'
ts_access='192.168.135.108'
realm='ims.mnc004.mcc204.3gppnetwork.org'
curl -v \
-H "User-Agent: 3gpp-gba" \
-H "Accept-Charset: *" \
-H 'X-3GPP-Asserted-Identity: "sip:$ue@$realm"' \
-H 'X-XCAP-Asserted-Identity: "sip:$ue@$realm"' \
http://$ts_access/simservs.ngn.etsi.org/users/sip:$ue@$realm/simservs.xml/~~/simservs/communication-diversion
# end

# from ts to mtas
ue='+31611808148'
ts_access='10.163.45.4'
realm='ims.mnc001.mcc272.3gppnetwork.org'
curl -vvvvv -k \
-H "User-Agent: 3gpp-gba" \
-H "Accept-Charset: *" \
-H "X-3GPP-Asserted-Identity: sip:$ue@$realm" \
-H "X-XCAP-Asserted-Identity: sip:$ue@$realm" \
-H "Host: xcap.ims.mnc001.mcc272.pub.3gppnetwork.org" \
https://$ts_access:8443/mtasxdms/simservs.ngn.etsi.org/users/sip:$ue@$realm/simservs.xml/~~/simservs/communication-diversion
# end

