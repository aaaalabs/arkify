# Arkify Landing Page

Ultra-minimal static landing page for arkify.app

## Deploy to Vercel

```bash
cd landing
vercel --prod
```

## Domain Setup

1. Deploy with Vercel CLI
2. Go to Vercel Dashboard → Project Settings → Domains
3. Add custom domain: `arkify.app`
4. Update DNS:
   - Type: `A`
   - Name: `@`
   - Value: `76.76.21.21` (Vercel IP)

   OR

   - Type: `CNAME`
   - Name: `@`
   - Value: `cname.vercel-dns.com`

5. Wait for DNS propagation (~5-60 minutes)

## Files

- `index.html` - 80 lines of pure HTML/CSS
- `phase1-final.png` - Latest phase output
- `vercel.json` - Cache headers
- Zero dependencies, zero build time

## Update Process

When new phase is complete:
1. Replace `phase1-final.png` with latest
2. `vercel --prod`
3. Done.
