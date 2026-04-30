# SHA-256 Hashing & Salting Demo

A minimal Flask web app that demonstrates plaintext handling, SHA-256 hashing, and salted hashing.

## Overview

This project is built for learning. It shows how input changes when moving from insecure plaintext to hashed and salted outputs. Everything runs through a simple web interface.

## Features

Plaintext output for direct comparison
SHA-256 hashing
SHA-256 with user-provided salt
Side-by-side comparison of hashed and salted results
Basic input validation

## Implementation

Backend is built with Python using Flask.
Frontend uses standard HTML and CSS.
Hashing is handled with Python’s built-in `hashlib` (SHA-256).

## How It Works

Enter text, then choose a mode.
Plaintext returns the original input.
Hash generates a SHA-256 digest.
Hash + Salt combines input with a salt before hashing.
The result is displayed instantly on the same page.
