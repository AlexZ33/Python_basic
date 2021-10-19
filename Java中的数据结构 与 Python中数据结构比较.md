<table>
<thead>
<tr>
<th>java.util.List</th>
<th>python.list</th>
</tr>
</thead>
<tbody>
<tr>
<td>List ls = new ArrayList();</td>
<td>ls = list()</td>
</tr>
<tr>
<td>ls.size()</td>
<td>len(ls)</td>
</tr>
<tr>
<td>ls.isEmpty()</td>
<td>not ls</td>
</tr>
<tr>
<td>ls.contains(e)</td>
<td>e in ls</td>
</tr>
<tr>
<td>ls.toArray()</td>
<td>list(ls)</td>
</tr>
<tr>
<td>ls.add(e)</td>
<td>ls.append(e)</td>
</tr>
<tr>
<td>ls.remove(e)</td>
<td>ls.remove(e)</td>
</tr>
<tr>
<td>ls.containsAll(lo)</td>
<td>all([e in ls for e in lo])</td>
</tr>
<tr>
<td>ls.addAll(lo)</td>
<td>ls.extend(lo)</td>
</tr>
<tr>
<td>ls.removeAll(lo)</td>
<td>[e for e in ls if e not in lo]</td>
</tr>
<tr>
<td>ls.replaceAll(operator)</td>
<td>list(map(key=operator,ls))</td>
</tr>
<tr>
<td>ls.sort()</td>
<td>ls.sort()</td>
</tr>
<tr>
<td>ls.clear()</td>
<td>ls.clear()</td>
</tr>
<tr>
<td>ls.get(i)</td>
<td>ls[i]</td>
</tr>
<tr>
<td>ls.set(i,e)</td>
<td>ls[i] = e</td>
</tr>
<tr>
<td>ls.add(i,e)</td>
<td>ls.insert(i,e)</td>
</tr>
<tr>
<td>ls.remove(i)</td>
<td>ls.pop(i)</td>
</tr>
<tr>
<td>ls.indexOf(e)</td>
<td>ls.index(e)</td>
</tr>
<tr>
<td>ls.subList(start,end)</td>
<td>ls[start:end]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>java.util.Set</th>
<th>python.set</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set st = new HashSet()</td>
<td>st = set()</td>
</tr>
<tr>
<td>st.size()</td>
<td>len(st)</td>
</tr>
<tr>
<td>st.isEmpty()</td>
<td>not st</td>
</tr>
<tr>
<td>st.contains(e)</td>
<td>e in st</td>
</tr>
<tr>
<td>st.toArray()</td>
<td>list(st)</td>
</tr>
<tr>
<td>st.add(e)</td>
<td>st.add(e)</td>
</tr>
<tr>
<td>st.remove(e)</td>
<td>st.discard(e) or st.remove(e)</td>
</tr>
<tr>
<td>st.containsAll(se)</td>
<td>st.issupperset(se)</td>
</tr>
<tr>
<td>st.retainAll(se)</td>
<td>st.intersection(se)</td>
</tr>
<tr>
<td>st.addAll(se)</td>
<td>st.union(se)</td>
</tr>
<tr>
<td>st.removeAll(se)</td>
<td>st.difference(se)</td>
</tr>
<tr>
<td>st.clear()</td>
<td>st.clear()</td>
</tr>
<tr>
<td>st.equals(se)</td>
<td>st == se</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>java.util.Map</th>
<th>python.dict</th>
</tr>
</thead>
<tbody>
<tr>
<td>Map d = new HashMap();</td>
<td>d = dict()</td>
</tr>
<tr>
<td>d.size()</td>
<td>len(d)</td>
</tr>
<tr>
<td>d.isEmpty()</td>
<td>not d</td>
</tr>
<tr>
<td>d.containsKey(k)</td>
<td>k in d or k in d.keys()</td>
</tr>
<tr>
<td>d.containsValue(v)</td>
<td>v in d.values()</td>
</tr>
<tr>
<td>d.get(k)</td>
<td>d.get(k) or d[k]</td>
</tr>
<tr>
<td>d.put(k,v)</td>
<td>d[k] = v or d.set(k,v)</td>
</tr>
<tr>
<td>d.remove(k)</td>
<td>d.remove(k) or d.pop(k)</td>
</tr>
<tr>
<td>d.putAll(d2)</td>
<td>d.update(d2)</td>
</tr>
<tr>
<td>d.clear()</td>
<td>d.clear()</td>
</tr>
<tr>
<td>d.keySet()</td>
<td>d.keys()</td>
</tr>
<tr>
<td>d.values()</td>
<td>d.values()</td>
</tr>
<tr>
<td>d.entrySet()</td>
<td>d.items()</td>
</tr>
<tr>
<td>d.equals(d2)</td>
<td>d == d2</td>
</tr>
<tr>
<td>d.getOrDefault(k,default)</td>
<td>d.get(k,default)</td>
</tr>
<tr>
<td>d.replace(k,v)</td>
<td>d[k] = v</td>
</tr>
</tbody>
</table>