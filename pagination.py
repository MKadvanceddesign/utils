def paginate(items, page=1, limit=50):
    """Return a single page of items.

    Args:
        items: Sequence to paginate.
        page:  1-based page number.
        limit: Maximum number of items per page.

    Returns:
        dict with keys: data, page, limit, total, total_pages.
    """
    total = len(items)
    total_pages = max(1, -(-total // limit))  # ceiling division
    start = (page - 1) * limit
    end = start + limit

    return {
        "data": items[start:end],
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
    }
