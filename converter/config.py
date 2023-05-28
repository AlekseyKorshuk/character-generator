base_prompt = '''

---
{{~! display the few-shot examples ~}}
{{~#each examples}}
Initial config:
{{this.inputs}}
Converted config:
{{this.outputs}}
---
{{~/each}}
Initial config:
{{query}}
Converted config:
'''
