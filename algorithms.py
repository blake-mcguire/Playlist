
def linear_search(songs, query, key='name'):
    results = []
    for song in songs:
        if getattr(song, key) == query:
            results.append(song)
    return results


def binary_search(songs, query, key='name'):
    left, right = 0, len(songs) - 1
    results = []
    while left <= right:
        mid = (left + right) // 2
        if getattr(songs[mid], key) == query:
            results.append(songs[mid])
            l, r = mid - 1, mid + 1
            while l >= left and getattr(songs[l], key) == query:
                results.append(songs[l])
                l -= 1
            while r <= right and getattr(songs[r], key) == query:
                results.append(songs[r])
                r += 1
            break
        elif getattr(songs[mid], key) < query:
            left = mid + 1
        else:
            right = mid - 1
    return results


def merge_sort(songs, key='name'):
    if len(songs) <= 1:
        return songs

    mid = len(songs) // 2
    left = merge_sort(songs[:mid], key)
    right = merge_sort(songs[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
