![kedro-local-notify-logo](static/logo.png)

# kedro-local-notify

![github-action](https://github.com/mzjp2/kedro-local-notify/workflows/Lint%20and%20test/badge.svg)
![code-style](https://img.shields.io/badge/code%20style-black-000000.svg)
![license](https://img.shields.io/badge/License-MIT-green.svg)

## How do I get started?

```console
$ pip install --upgrade kedro-local-notify
```

### Then what?

Nothing! Kedro will automagically pick up the hook and ping you a notification after the pipeline finished running succesfully or fails.

## What is `kedro-local-notify`?

Ever kicked off a long-running pipeline and come back to check in an hour later, only to find that it failed 2 minutes in?

Or come back to see your pipeline finished running an hour ago and you have nothing to justify your reddit browsing anymore?

`kedro-local-notify` will ping you a notification indicating that your pipeline ran sucessfully or failed.

![kedro-local-notify-demo](static/demo.png)

## Won't this spam me?

By default, notifications will only trigger if the pipeline has been running for more than 1 minute. You can change this thresholf for notifying you by setting the `KEDRO_LOCAL_NOTIFY_THRESHOLD` environment variable to be the number of seconds of pipeline run time before a notification is trigerred. The default is:

```console
$ export KEDRO_LOCAL_NOTIFY=60
```

note that this environment variable needs to be set in the same shell that you're trigerring the Kedro pipeline run in.

## Caveats

You probably shouldn't add this to your requirements. It's a silly little tool meant to be used for some quality of life improvements on your local machine.

This is currently limited to Mac OS X 10.10 or higher. Windows support is in the works!
