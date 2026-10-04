# IPO Radar Lite (starter)

A standard-library Python script that sends one short Telegram message on the IPO days that matter: closing today, allotment (T+1), refund or credit (T+2), listing (T+3), opening soon, plus new IPO headlines from the ipowatch RSS feed. It reads your `watchlist.csv`; you or Kiro keep that file up to date.

It **never** places bids or orders, logs in anywhere, or stores PAN, UPI IDs, bank, demat or application numbers. Full walkthrough: section 30 of the [HTML guide](../../ipo/ipo-start-to-automation-guide.html#auto3).

| File | Use |
|---|---|
| `radar_lite.py` | The bot. `--self-test`, `--dry-run`, `--date`, `--job test` and `--today-context` help you check it |
| `watchlist.example.csv` | Example rows (October 2026). Copy to `watchlist.csv` in your private repo |
| `radar-lite.workflow.yml` | GitHub Actions schedule. Save as `.github/workflows/radar-lite.yml` in your **private** repo |

## Set up from a private repo

1. Copy `.kiro/`, `ipo/` and `ipo-radar/` from this repository into your private repo.
2. Rename `ipo-radar/lite/watchlist.example.csv` to `watchlist.csv`.
3. Move `ipo-radar/lite/radar-lite.workflow.yml` to `.github/workflows/radar-lite.yml`.
4. Add the Actions secrets `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
5. Go to **Actions → IPO Radar Lite → Run workflow** and choose `job: test`.

The workflow refuses to run from a public repository, because your watchlist shows what you applied for.

## Check it locally

```bash
python3 ipo-radar/lite/radar_lite.py --self-test
python3 ipo-radar/lite/radar_lite.py --job morning --dry-run --date 2026-10-05 --watchlist ipo-radar/lite/watchlist.example.csv
```

`watchlist.csv` columns: `name, board (mainboard|sme), open, close (YYYY-MM-DD), allotment, listing (optional: computed as T+1 and T+3), lot_size, price_high, registrar, label (apply|watch|skip), score, status (watching|paper|applied|allotted|not_allotted|sold|skipped), exit_plan, notes`. Wrap any cell that contains a comma in double quotes.

NSE holidays for 2026 are built in. When NSE publishes the 2027 list (usually in December), add the dates to `ipo-radar/lite/nse-holidays.txt`, one `YYYY-MM-DD Name` per line.

Not investment advice. You bid manually and approve the UPI mandate yourself.
