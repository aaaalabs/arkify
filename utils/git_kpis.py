"""
Git-Based KPI Extraction

Extracts authentic development metrics from Git history.
Use this for generating accurate Phase breakdowns.
"""

import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional


class GitKPIExtractor:
    """Extract development KPIs from Git repository history."""

    def __init__(self, repo_path: Optional[Path] = None):
        """
        Initialize Git KPI extractor.

        Args:
            repo_path: Path to git repository (defaults to current directory)
        """
        self.repo_path = repo_path or Path.cwd()

    def _run_git_command(self, cmd: List[str]) -> str:
        """
        Run git command and return output.

        Args:
            cmd: Git command as list of arguments

        Returns:
            Command output as string

        Raises:
            RuntimeError: If git command fails
        """
        try:
            result = subprocess.run(
                ['git'] + cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git command failed: {e.stderr}") from e

    def get_first_commit_time(self) -> datetime:
        """
        Get timestamp of first commit.

        Returns:
            Datetime of first commit
        """
        timestamp_str = self._run_git_command([
            'log', '--all', '--pretty=format:%ai', '--reverse'
        ]).split('\n')[0]
        return datetime.fromisoformat(timestamp_str)

    def get_latest_commit_time(self) -> datetime:
        """
        Get timestamp of latest commit.

        Returns:
            Datetime of latest commit
        """
        timestamp_str = self._run_git_command([
            'log', '--all', '--pretty=format:%ai', '-1'
        ])
        return datetime.fromisoformat(timestamp_str)

    def get_total_commits(self) -> int:
        """
        Get total number of commits.

        Returns:
            Total commit count
        """
        output = self._run_git_command(['rev-list', '--all', '--count'])
        return int(output)

    def get_commits_by_author(self) -> Dict[str, int]:
        """
        Get commit counts grouped by author.

        Returns:
            Dict mapping author name to commit count
        """
        output = self._run_git_command([
            'log', '--all', '--pretty=format:%an'
        ])
        authors: Dict[str, int] = {}
        for author in output.split('\n'):
            authors[author] = authors.get(author, 0) + 1
        return authors

    def get_files_changed(self) -> int:
        """
        Get total number of files changed across all commits.

        Returns:
            Total files changed count
        """
        output = self._run_git_command([
            'log', '--all', '--pretty=format:', '--name-only'
        ])
        unique_files = set(f for f in output.split('\n') if f.strip())
        return len(unique_files)

    def get_lines_added_removed(self) -> Dict[str, int]:
        """
        Get total lines added and removed.

        Returns:
            Dict with 'added' and 'removed' line counts
        """
        output = self._run_git_command([
            'log', '--all', '--pretty=tformat:', '--numstat'
        ])

        added = 0
        removed = 0

        for line in output.split('\n'):
            if not line.strip():
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                try:
                    added += int(parts[0]) if parts[0] != '-' else 0
                    removed += int(parts[1]) if parts[1] != '-' else 0
                except ValueError:
                    continue

        return {'added': added, 'removed': removed}

    def get_commit_messages(self, limit: Optional[int] = None) -> List[str]:
        """
        Get commit messages.

        Args:
            limit: Maximum number of messages to return (None for all)

        Returns:
            List of commit messages
        """
        cmd = ['log', '--all', '--pretty=format:%s']
        if limit:
            cmd.append(f'-{limit}')

        output = self._run_git_command(cmd)
        return [msg for msg in output.split('\n') if msg.strip()]

    def calculate_development_hours(self) -> float:
        """
        Calculate total development hours from first to latest commit.

        Assumes continuous development during commit timespan.
        For more accurate tracking, use commit frequency analysis.

        Returns:
            Total hours between first and last commit
        """
        first = self.get_first_commit_time()
        latest = self.get_latest_commit_time()
        duration = latest - first
        return duration.total_seconds() / 3600

    def get_phase_kpis(self, phase_tag: Optional[str] = None) -> Dict[str, Any]:
        """
        Extract comprehensive KPIs for a development phase.

        Args:
            phase_tag: Git tag marking phase completion (e.g., 'v0.0.1')
                      If None, uses all commits

        Returns:
            Dict with all phase KPIs
        """
        first_commit = self.get_first_commit_time()
        latest_commit = self.get_latest_commit_time()
        total_hours = self.calculate_development_hours()

        lines = self.get_lines_added_removed()
        total_lines = lines['added'] - lines['removed']

        return {
            'development': {
                'start_date': first_commit.strftime('%Y-%m-%d'),
                'end_date': latest_commit.strftime('%Y-%m-%d'),
                'start_time': first_commit.strftime('%H:%M'),
                'end_time': latest_commit.strftime('%H:%M'),
                'total_hours': round(total_hours, 1),
                'duration_days': (latest_commit - first_commit).days,
            },
            'commits': {
                'total': self.get_total_commits(),
                'by_author': self.get_commits_by_author(),
                'messages': self.get_commit_messages(limit=10),
            },
            'code': {
                'files_changed': self.get_files_changed(),
                'lines_added': lines['added'],
                'lines_removed': lines['removed'],
                'net_lines': total_lines,
            },
            'meta': {
                'extracted_at': datetime.now().isoformat(),
                'repo_path': str(self.repo_path),
                'phase_tag': phase_tag,
            }
        }

    def generate_phase_summary(self) -> str:
        """
        Generate human-readable phase summary.

        Returns:
            Formatted summary string
        """
        kpis = self.get_phase_kpis()
        dev = kpis['development']
        commits = kpis['commits']
        code = kpis['code']

        summary = f"""
Phase Development Summary
=========================

📅 Timeline:
   Start: {dev['start_date']} at {dev['start_time']}
   End:   {dev['end_date']} at {dev['end_time']}
   Duration: {dev['total_hours']} hours ({dev['duration_days']} days)

💻 Commits:
   Total commits: {commits['total']}
   Authors: {', '.join(f"{a} ({c})" for a, c in commits['by_author'].items())}

📝 Code Changes:
   Files changed: {code['files_changed']}
   Lines added: {code['lines_added']:,}
   Lines removed: {code['lines_removed']:,}
   Net lines: {code['net_lines']:,}

Recent Commits:
{''.join(f"   - {msg}\n" for msg in commits['messages'][:5])}
"""
        return summary.strip()


def extract_kpis_for_yaml(repo_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Extract KPIs formatted for Arkify YAML input.

    Args:
        repo_path: Path to git repository

    Returns:
        Dict suitable for project YAML extended fields
    """
    extractor = GitKPIExtractor(repo_path)
    kpis = extractor.get_phase_kpis()

    return {
        'timeline': {
            'start_date': kpis['development']['start_date'],
            'end_date': kpis['development']['end_date'],
            'total_hours': kpis['development']['total_hours'],
            'duration_days': kpis['development']['duration_days'],
        },
        'git_stats': {
            'total_commits': kpis['commits']['total'],
            'files_changed': kpis['code']['files_changed'],
            'lines_of_code': kpis['code']['net_lines'],
        },
        'reality_check': {
            'commits_per_hour': round(
                kpis['commits']['total'] / max(kpis['development']['total_hours'], 0.1),
                1
            ),
            'lines_per_commit': round(
                kpis['code']['net_lines'] / max(kpis['commits']['total'], 1),
                0
            ),
        }
    }


if __name__ == '__main__':
    # Example usage
    extractor = GitKPIExtractor()
    print(extractor.generate_phase_summary())
    print("\n\nYAML-Ready KPIs:")
    import json
    print(json.dumps(extract_kpis_for_yaml(), indent=2))
