class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 1
                email_to_name[email] = name
        for acc in accounts:
            first_email = acc[1]
            for email in acc[2:]:
                union(first_email, email)
        
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)
        res = []
        for root in groups:
            name = email_to_name[root]
            emails = sorted(groups[root])
            res.append([name] + emails)
        return res