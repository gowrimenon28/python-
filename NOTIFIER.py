from plyer import notification

title='Hello gowri'

message='stay positive'

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
