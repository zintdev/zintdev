# Setup

Copy these files and folders into the root of the `zintdev/zintdev` profile repository:

- `README.md`
- `assets/userstats.svg`
- `scripts/update_quote.py`
- `.github/workflows/profile-assets.yml`

Then:

1. Commit and push all files to the `main` branch.
2. Open the repository's **Actions** tab.
3. Select **Update profile assets**.
4. Choose **Run workflow**.
5. Ensure **Settings → Actions → General → Workflow permissions** allows **Read and write permissions** if the workflow cannot push.

The README references `./assets/userstats.svg`, a local repository file. The workflow regenerates that SVG daily, so profile rendering no longer depends on public Vercel image endpoints.

The trophy section uses native Markdown based on the GitHub achievements shown on the profile, and the quote is rotated from a local list. Neither section depends on an external image service.
