def includeme(config):
    config.include('.company', route_prefix='/v1')
    config.include('.customer', route_prefix='/v1')
