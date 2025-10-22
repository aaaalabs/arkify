"""
Icon Fetcher Agent
Phase 0: Fetch logos from SimpleIcons CDN

Fetches brand logos for tech stack visualization.
No API key needed - uses public CDN.
"""

import requests
from pathlib import Path
from typing import List, Dict, Any
from urllib.parse import quote


class IconFetcher:
    """
    Fetch and cache technology logos.

    Phase 0: SimpleIcons CDN only
    Phase 2: Add DevIcon, custom fallbacks
    Phase 4: Add brand color extraction
    """

    def __init__(self):
        """Initialize icon fetcher with cache."""
        self.cache_dir = Path('output/.icon_cache')
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # SimpleIcons CDN base URL
        self.simpleicons_base = "https://cdn.simpleicons.org"

        # Technology name normalization
        # Maps common names to SimpleIcons slugs
        self.name_mapping = {
            'nextjs': 'nextdotjs',
            'next.js': 'nextdotjs',
            'vercel': 'vercel',
            'supabase': 'supabase',
            'claude': 'anthropic',
            'cursor': 'cursor',  # Note: May not exist, will use fallback
            'react': 'react',
            'typescript': 'typescript',
            'python': 'python',
            'tailwind': 'tailwindcss',
            'stripe': 'stripe',
            'fastapi': 'fastapi',
            'github api': 'github',
        }

    def fetch(self, tech_stack: List[str]) -> List[Dict[str, Any]]:
        """
        Fetch icons for technology stack.

        Args:
            tech_stack: List of technology names

        Returns:
            List of icon metadata dictionaries
        """
        icons = []

        for tech in tech_stack[:4]:  # Limit to 4 for 2x2 grid
            icon_data = self._fetch_icon(tech)
            icons.append(icon_data)

        return icons

    def _fetch_icon(self, tech_name: str) -> Dict[str, Any]:
        """
        Fetch a single icon.

        Args:
            tech_name: Technology name

        Returns:
            Icon metadata dictionary
        """
        # Normalize name
        normalized = tech_name.lower().strip()
        slug = self.name_mapping.get(normalized, normalized)

        # Try to fetch from SimpleIcons CDN
        svg_url = f"{self.simpleicons_base}/{slug}"
        cache_path = self.cache_dir / f"{slug}.svg"

        # Check cache first
        if cache_path.exists():
            return {
                'name': tech_name,
                'slug': slug,
                'path': str(cache_path),
                'source': 'cache'
            }

        # Fetch from CDN
        try:
            response = requests.get(svg_url, timeout=5)
            if response.status_code == 200:
                # Save to cache
                cache_path.write_bytes(response.content)
                return {
                    'name': tech_name,
                    'slug': slug,
                    'path': str(cache_path),
                    'source': 'simpleicons'
                }
            else:
                # Icon not found, use fallback
                return self._create_fallback_icon(tech_name, slug)

        except Exception as e:
            print(f"    ⚠️  Could not fetch icon for '{tech_name}': {e}")
            return self._create_fallback_icon(tech_name, slug)

    def _create_fallback_icon(self, tech_name: str, slug: str) -> Dict[str, Any]:
        """
        Create a simple text-based fallback icon.

        Args:
            tech_name: Technology name
            slug: Normalized slug

        Returns:
            Fallback icon metadata
        """
        # Create simple SVG with first 2 letters
        initials = tech_name[:2].upper()

        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect width="100" height="100" fill="#667eea" rx="15"/>
  <text x="50" y="65" font-family="Arial, sans-serif" font-size="45" font-weight="bold"
        fill="white" text-anchor="middle">{initials}</text>
</svg>'''

        # Save fallback
        cache_path = self.cache_dir / f"{slug}_fallback.svg"
        cache_path.write_text(svg_content)

        return {
            'name': tech_name,
            'slug': slug,
            'path': str(cache_path),
            'source': 'fallback'
        }
