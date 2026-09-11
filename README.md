# Luo Zhou's Academic Homepage

Source code for [luozhou320.github.io](https://luozhou320.github.io), the academic homepage of **Luo Zhou (周骆)**, Postdoctoral Researcher in the Department of Computer Science and Engineering at The Hong Kong University of Science and Technology.

The site is built with [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) academic website template, then deployed automatically with GitHub Actions.

## Site features

- Responsive profile and biography layout for desktop and mobile
- Light and dark themes with a system-theme default
- News timeline with collapsible earlier entries
- Complete BibTeX-driven publication list and selected publications on the homepage
- Publication previews, abstracts, citation counts, PDFs, slides, posters, code, and external links
- Dedicated Awards, Services, and CV pages
- Automatic Google Scholar citation updates
- Google Analytics integration
- Accessible navigation and a document-flow footer that does not cover page content

## Content map

| Content                                               | File or directory                 |
| ----------------------------------------------------- | --------------------------------- |
| Biography, profile details, news, and homepage layout | `_pages/about.md`                 |
| Awards and honors                                     | `_pages/awards.md`                |
| Professional service                                  | `_pages/service.md`               |
| Education, experience, and research project           | `_data/cv.yml`                    |
| Publications and resource metadata                    | `_bibliography/papers.bib`        |
| Email and academic/social profiles                    | `_data/socials.yml`               |
| Profile photograph                                    | `assets/img/prof_pic.jpg`         |
| Publication thumbnails                                | `assets/img/publication_preview/` |
| CV, papers, slides, and posters                       | `assets/pdf/`                     |
| Site settings, analytics, and layout options          | `_config.yml`                     |

## Local development

The current setup uses Ruby 3.3, Bundler 4, and Node.js 24. From the repository root, install the dependencies and start the local server:

```bash
bundle install
npm ci
bash run_server.sh
```

Open [http://127.0.0.1:4000](http://127.0.0.1:4000). Content and style changes are reloaded automatically; restart the server after changing `_config.yml`.

Before publishing, run the same core checks used during local development:

```bash
npm run lint:prettier
npm run lint:style-contract
bundle exec jekyll build --config _config.yml,_config_dev.yml
```

## Updating publications

Add or edit entries in `_bibliography/papers.bib`. Common optional fields include:

```bibtex
preview           = {paper-preview.png},
pdf               = {paper.pdf},
slides            = {slides.pdf},
poster            = {poster.pdf},
code              = {https://github.com/example/project},
video             = {https://example.com/demo},
website           = {https://example.com/project},
abstract          = {A concise summary of the paper.},
google_scholar_id = {ScholarPublicationId},
selected          = {true}
```

Place preview images in `assets/img/publication_preview/` and local publication resources in `assets/pdf/`. Setting `selected = {true}` displays the paper on the homepage as well as on the complete Publications page.

## Citation updates

The `Update Google Scholar Citations` workflow runs daily and can also be started manually from the repository's **Actions** tab. It reads the Scholar profile ID from `_data/socials.yml`, matches publications using `google_scholar_id`, and updates `_data/citations.yml`.

If Google Scholar is temporarily unavailable, the workflow preserves the last successful citation snapshot and retries on the next scheduled run.

## Deployment

Changes pushed to `main` trigger `.github/workflows/deploy.yml`. The workflow builds the production site and publishes the generated `_site` directory to the `gh-pages` branch. GitHub Pages should be configured to serve from that branch.

## Credits

This personal site is based on [al-folio](https://github.com/alshedivat/al-folio). See [LICENSE](LICENSE) for the repository license.
