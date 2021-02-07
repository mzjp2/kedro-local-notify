"""The hook definitions for kedro-local-notify"""
import os
import time
from pathlib import Path
from typing import Any, Dict

import pync
from kedro.framework.hooks import hook_impl
from kedro.pipeline import Pipeline

APP_ICON = Path(__file__).parent / "static" / "kedro.png"
NOTIFICATION_THRESHOLD = int(os.getenv("KEDRO_LOCAL_NOTIFY_THRESHOLD", "60"))


class KedroLocalNotifyHooks:
    """The hook class for kedro local notify.

    Implements the pipeline error and run hooks.
    """

    def __init__(self):
        self._start_time = None

    @hook_impl
    def before_pipeline_run(self):
        """Starts the pipeline run timer"""
        self._start_time = time.time()

    @hook_impl
    def on_pipeline_error(self, error, run_params: Dict[str, Any]):
        """Triggers the pipeline error notifcation"""
        self._kedro_notify(
            run_params=run_params,
            subtitle="❌ Failed",
            message=f"failed with error {error}",
        )

    @hook_impl
    def after_pipeline_run(self, run_params: Dict[str, Any], pipeline: Pipeline):
        """Triggers the pipeline successful run notification"""
        num_nodes = len(pipeline.nodes)
        self._kedro_notify(
            run_params=run_params,
            subtitle="✅ Finished",
            message=f"finished sucesfully with {num_nodes} nodes executed",
        )

    def _kedro_notify(self, subtitle: str, run_params: Dict[str, Any], message: str):
        pipeline_run_time = time.time() - self._start_time
        if pipeline_run_time < NOTIFICATION_THRESHOLD:
            return

        pipeline_name = run_params.get("pipeline_name")
        if pipeline_name:
            message = f"Your pipeline {pipeline_name}: {message}"
        else:
            message = f"Your pipeline: {message}"

        pync.notify(
            title="Kedro",
            subtitle=f"{subtitle} in {pipeline_run_time:.2f}s",
            message=message,
            appIcon=str(APP_ICON),
        )


hooks = KedroLocalNotifyHooks()
