#!/bin/bash

for PYTHON in 2.5 2.6 2.7 pypy 3.2; do
    echo "Nosetesting $PYTHON"
    nosetests-$PYTHON $@
done
