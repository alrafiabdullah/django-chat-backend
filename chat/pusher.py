import pusher

pusher_client = pusher.Pusher(
    app_id='app_id',
    key='key',
    secret='secret',
    cluster='cluster',
    ssl=True
)
