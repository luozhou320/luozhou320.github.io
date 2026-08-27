# Publication resources

Store publication resources with short, lowercase filenames. Configure their
paths in `_data/publications.yml`; a button is displayed only when its field is
present.

Recommended locations:

- Paper PDF: `/files/publications/paper-name.pdf`
- Slides: `/files/publications/slides/paper-name-slides.pdf`
- Poster: `/files/publications/posters/paper-name-poster.pdf`
- Code archive: `/files/publications/code/paper-name-code.zip`
- Local demo: `/files/publications/demos/paper-name-demo.mp4`

For code repositories and online demos, use the complete external URL instead:

```yaml
code: https://github.com/username/repository
demo: https://www.youtube.com/watch?v=example
```

Example using local resources:

```yaml
slides: /files/publications/slides/baro2talk-slides.pdf
poster: /files/publications/posters/baro2talk-poster.pdf
code: /files/publications/code/baro2talk-code.zip
demo: /files/publications/demos/baro2talk-demo.mp4
```
