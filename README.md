# Consul agent client for python

Any python service can register and send heartbeats to consul agent.

WARNING: This module is for python2 and doesn't maintained anymore. 
For python3 see https://github.com/dkdhub/py-consul-tiny

# Usage with tornado

```
    from tornado.ioloop import PeriodicCallback
    from consul.agent import ConsulAgent, HTTPError

    consul = ConsulAgent()

    def heartbeat():
        try:
            consul.check_update_with_register(
                'my_service:ttl_check',
                id='my_service',
                address='127.0.0.1',
                port=8080,
                checks=[{
                    'CheckId': 'my_service:ttl_check',
                    'TTL': '40s',
                    'DeregisterCriticalServiceAfter': 15m,
                }],
            )
        except HTTPError, e:
            from tornado.log import app_log as log
            log.warning("failed to heartbeat to consul:", "%s %s" % (
                e.response.status_code, e.response.content) if e.response.content else unicode(e))

    # deregister old service if any to force service update
    consul.service_deregister('my_service')
    heartbeat()
    PeriodicCallback(heartbeat, 3000).start()
```
