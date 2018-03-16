#!/bin/bash

wget -O - $1 | sha256sum -b -
