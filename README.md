# Consul agent client for python

# Usage with tornado

```
    from tornado.ioloop import PeriodicCallback
    from consul.agent import ConsulAgent

    consul = ConsulAgent()

    def heartbeat():
        consul.service_register(
            id='backend',
            port=8081,
            checks=[
                # this check must be updated from sevice
                {
                    'CheckId': 'backend_ttl_check',
                    'TTL': '40s',
                    'DeregisterCriticalServiceAfter': '10m',    # agent will unregister service
                },
                # check response status to be 200
                {
                    'Args': ['curl', '127.0.0.1:8081/api/v1'],
                    'Interval': '30s',
                }
            ],
        )

        # notify ttl check
        consul.check_update('backend_ttl_check')

    heartbeat()
    PeriodicCallback(heartbeat, 30000).start()
```
