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

chat_prompt = '''

{{~! display the few-shot examples ~}}
{{~#each examples}}

{{#user~}}
{{this.inputs}}
{{~/user}}

{{#assistant~}}
{{this.outputs}}
{{~/assistant}}

{{~/each}}

{{#user~}}
{{query}}
{{~/user}}

{{#assistant~}}
{{gen 'result' max_tokens=1536 temperature=0}}
{{~/assistant}}
'''
