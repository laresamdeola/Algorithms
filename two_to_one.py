def longest(a1, a2):
    return ''.join(sorted(set(sorted(set(a1)) + sorted(set(a2)))))
  
longest("aretheyhere", "yestheyarehere")