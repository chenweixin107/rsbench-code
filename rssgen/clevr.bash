#!/usr/bin/env bash

cd rssgen/clevr || exit 1

for seed in $(seq 0 999); do
  echo "================================"
  echo "Running experiments with seed: $seed"
  echo "================================"

  Xvfb :$seed -screen 0 1024x768x24 &
  export DISPLAY=:$seed

  sleep 10  # wait for Xvfb to be ready

#  ~/workspace/blender-2.83.20-linux-x64/blender -noaudio -b -P clevr_renderer.py -- \
#    --config /home/jovyan/workspace/rsbench-code/rssgen/examples_config/clevr_3obj.yml \
#    --min_objects 3 --max_objects 3 \
#    --start_idx $((seed * 10)) \
#    --seed $seed

  ~/workspace/blender-2.83.20-linux-x64/blender -noaudio -b -P clevr_renderer.py -- \
    --config /home/jovyan/workspace/rsbench-code/rssgen/examples_config/clevr_5obj.yml \
    --min_objects 5 --max_objects 5 \
    --start_idx $((seed * 10)) \
    --seed $seed

  kill %1 # Optional: kill Xvfb after use
done
