# Liberty Immigration Council — site & blog setup / handoff

The full site is static (hand-written HTML + Tailwind CDN, no build to serve).
Blog articles are Markdown in `content/blog/` and are compiled to static HTML by
`_gen_blog.py` (runs locally and via the GitHub Action `.github/workflows/blog.yml`).
The blog is edited by a non-technical person through **Sveltia CMS** at `/admin/`.

## A. Move the repo to Anton's GitHub account

Option 1 — transfer (keeps history): GitHub → repo Settings → Danger Zone →
Transfer ownership → Anton's account.
Option 2 — fresh: Anton creates an empty repo and we push this code into it.

After moving, set the repo name in **one place**:
- `admin/config.yml` → `backend.repo:` → change to `ANTON_GH_USER/REPO_NAME`.
(That is the only repo-specific line.)

## B. Host on Cloudflare Pages (auto-deploy on every change)

Cloudflare dashboard → Workers & Pages → Create → Pages → **Connect to Git** →
pick the repo → Production branch: `main` →
**Build command: (leave empty)** · **Build output directory: `/`** → Save & Deploy.
Then add the custom domain `libertyimmigrationcouncil.org` to this Pages project.

From now on every push (our code, the blog Action, or a post saved in the CMS)
deploys automatically.

## C. Blog editor login (Sveltia CMS) — the nice "Sign in with GitHub" button

Anton edits posts at `https://libertyimmigrationcouncil.org/admin/`.
Two ways to sign in:

**Quick (no server): "Sign In Using Access Token"** — Anton creates a GitHub
fine-grained Personal Access Token with read/write to the repo and pastes it. Works
immediately, nothing to deploy. Token must belong to an account with write access to the repo.

**Nice button: "Sign In with GitHub"** (one-time setup, free, on Cloudflare):
1. GitHub → Settings → Developer settings → OAuth Apps → New OAuth App.
   - Homepage URL: `https://libertyimmigrationcouncil.org`
   - Authorization callback URL: `https://sveltia-cms-auth.<your-subdomain>.workers.dev/callback`
   - Save the **Client ID** and generate a **Client secret**.
2. Deploy the free auth worker `sveltia-cms-auth`
   (https://github.com/sveltia/sveltia-cms-auth — "Deploy to Cloudflare" button).
   Set worker variables: `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`,
   `ALLOWED_DOMAINS=libertyimmigrationcouncil.org`.
3. In `admin/config.yml`, under `backend:` add:
   `base_url: https://sveltia-cms-auth.<your-subdomain>.workers.dev`
   Commit. Done — the "Sign in with GitHub" button now works.

## D. What's already done (no action needed)

- All site pages (home, attorney, services, success stories, foundations,
  corporate giving, annual report, board, thank-you, privacy, accessibility).
- EIN 41-5367566 published site-wide.
- Blog: index `blog.html` + article template, 2 starter articles, "Blog" in nav + footer.
- Sveltia CMS at `/admin/` with a **live preview that renders posts in the real site style**.
- GitHub Action auto-rebuilds the blog HTML whenever a post is added/edited.

## E. Adding a blog post (for Anton, after login)

`/admin/` → Blog posts → New → fill Title, Date, Author, Short summary, optional
Cover image, write the Article (you see it in the real style on the right) → Publish.
The post goes live automatically in a minute or two.
