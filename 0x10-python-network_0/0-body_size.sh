#!/bin/bash
# Gets byte size of the HTTP response body for a given URL.
curl -s -o /dev/null -w "%{size_download}" "$1"
