# Public export boundary
public-package-allowlist.json is the explicit file-by-file export authority. Export only these regular files from the standalone private source. Never copy a parent project, registry, gateway implementation, credentials or customer content.
Release metadata is a sidecar, excluded from its own ZIP to avoid a circular hash. Build time is the source commit timestamp. One build produces the immutable asset copied to all three locations.
