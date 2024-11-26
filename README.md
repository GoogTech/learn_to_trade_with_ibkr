## Some questions about IBKR’s Client Portal API 
### 1.How can I prevent the session from timing out?
A Client Portal API brokerage session will timeout if no requests are received within a period of 5 minutes. In order to prevent the session from timing out, the endpoint /tickle should be called on a regular basis. It is recommended to call this endpoint approximately every minute.

If the brokerage session has timed out but the session is still connected to the IBKR backend, the response to /auth/status returns ‘connected’:true and ‘authenticated’:false. Calling the /reauthenticate endpoint will start a new brokerage session.


### 2.How long does a session remain authenticated?
A session can remain authenticated for up to 24 hours, resetting at midnight for New York, U.S.; Zug, Switzerland; or Hong Kong time depending on your nearest connection.

Sessions will time out after approximately 6 minutes without sending new requests or maintaining the /tickle endpoint at least every 5 minutes.

Daily maintenance of IBKR’s servers could result in a disconnect earlier than the 24 hour period mentioned above. We advise disconnecting your session from your gateway and restarting it after the maintenance time to minimize any potential problems that may arise. Information on server reset times and system status updates can be found on the System Staus page.

> Web API v1.0 Doc : https://www.interactivebrokers.com/campus/ibkr-api-page/cpapi-v1/#auth-faq