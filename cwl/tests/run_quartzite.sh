#!/bin/bash

CWL="cwl/quartzite.cwl"
YAML="cwl/tests/quartzite_config.yaml"

mkdir -p cwl/tests/test_results
RABIX_ARGS="--basedir cwl/tests/test_results"

rabix $RABIX_ARGS $CWL $YAML
