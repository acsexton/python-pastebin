# Pastebin in Python / Django REST Framework

This is a simple pastebin/code snippets implementation built in Python using Django REST Framework.

It uses standard RESTful API approaches to manage creation, display, updating, and deletion of code
snippets (featuring syntax highlighting with `pygments`). It allows different interactions based on
ownership of a given snippet, automatically handles URL endpoints for new snippets, and the secret
key is managed by dotenv implementation.

It started a bit more complicated (as git commit history will show) than its current state, but
heavily simplified itself as I learned more about DRF's supported viewsets, modeling approaches, and
generics.
