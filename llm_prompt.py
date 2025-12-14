# import json


# class LLMPrompt:
#     def __init__(self):
#         self.user_results = []

#     def prompt_for_user_based_search(self, search_result):
#         for key, value in search_result["user_based_search"].items():
#             for entry in value:
#                 self.user_results.append(entry)

#         user_query_llm_input = json.dumps(self.user_results, indent=4)

#         prompt = f'''
#         I am providing a JSON containing text excerpts that match a user's query with a similarity score of 0.85 or higher. Your task is to generate concise, well-structured, and contextually relevant headings, sub-headings, and summaries based on this content.

#         ### Instructions:
#         - Extract headings from the "sub-heading" key in the provided JSON, removing any initial numbers or prefixes.
#         - If multiple "sub-headings" share the same core idea, provide distinct headings and unique summaries for each perspective.
#         - Include relevant sub-headings under their respective headings using the Markdown "###" format.
#         - Ensure headings, sub-headings, and summaries are clear, concise, and directly relevant to the user’s query.
#         - Retain key insights while eliminating redundancy and unnecessary details.
#         - Synthesize different perspectives from the content into unified, coherent summaries where applicable.
#         - Ensure the output is structured for accurate LaTeX conversion:
#             - Use `$...$` for inline formulas (e.g., `$E = mc^2$`).
#             - Use `$$...$$` for block-level formulas.
#             - Maintain proper nesting of headings and sub-headings.

#         ### Input:
#             {user_query_llm_input}

#         ### Output Format:
#         - Use Markdown format for headings (##) and sub-headings (###).
#         - Each heading should be followed by its corresponding sub-headings and summary.
#         - Ensure formulas are formatted correctly for LaTeX conversion.
#         - Provide unique summaries for each heading without repeating information.

#         ### Example Output:

#         ## 1 Main Heading
#         Brief introductory summary.

#         ### 1.1 Sub-heading
#         Concise summary with key insights.

#         ### 1.2 Another Sub-heading
#         Further insights under the same heading.

#         $$ a^2 + b^2 = c^2 $$

#         ## 2 Second Main Heading
#         Another introductory summary.

#         ### 2.1 Sub-heading
#         Detailed explanation with a formula:

#         $E = mc^2$
#         '''

#         with open('./extracted/userbased.txt','w',encoding='utf-8') as data:
#             data.write(str(prompt))

#         return prompt
    

#     def prompt_for_intro(self, search_result):
#         intros =  search_result.get("default_results", {}).get("Introduction", {})
#         if not intros:  
#             intros = search_result["user_based_search"].items()

#         intro_formatted_data = {"Introduction": intros}

#         # Convert to JSON string
#         prompt = f'''
#             I am providing a JSON containing introductions from multiple academic papers, along with their similarity scores. Your task is to generate a concise, well-structured, and academically written summarized introduction that effectively presents the background, motivation, and objectives of the given papers.

#             Instructions:
#             - The summary should be formal, academic, and engaging.
#             - Clearly introduce the topic, research problem, and significance of the study.
#             - Retain key background information while avoiding redundancy.
#             - Ensure logical coherence and a smooth transition of ideas.
#             - Highlight common themes, research gaps, and objectives from the provided texts.
            
#             Input: {intro_formatted_data}

#             Note:  Do not include text like I understand or here is your summary and Do not mension heading at start.

#             Output Format:
#             Provide a well-structured and academically written introduction that encapsulates the key elements of the provided introductions.
#         '''
#         with open('./extracted/introduction.txt','w',encoding='utf-8') as data:
#             data.write(str(prompt))

#         return prompt
    
#     def prompt_for_abstract(self, search_result):
#         abstracts =  search_result.get("default_results", {}).get("Abstract", {})

#         if not abstracts:  
#             abstracts = search_result["user_based_search"].items()

#         abstract_formatted_data = {"Abstract": abstracts}

#         # Convert to JSON string
#         abstract_llm_input = json.dumps(dict(abstract_formatted_data), indent=4)

#         prompt = f'''
#             I am providing a JSON containing abstracts from multiple academic papers, along with their similarity scores. Your task is to generate a concise, well-structured, and academically written summarized abstract that captures the core ideas, key findings, and main contributions of the given abstracts.

#             Instructions:
#             - The summary should be formal and academic in tone.
#             - Retain the most significant insights from the abstracts while eliminating redundancy.
#             - Ensure the summary is coherent and logically structured, maintaining a clear flow of ideas.
#             - Where applicable, highlight any common themes, key methodologies, or conclusions.
#             - Avoid unnecessary details while ensuring completeness and clarity.
            
#             Input: {abstract_llm_input}

#             Note:  Do not include text like I understand or here is your summary and Do not mension heading at start.

#             Output Format:
#             Provide a single summarized abstract in clear, academic language.
#         '''
        
#         with open('./extracted/abstract.txt','w',encoding='utf-8') as data:
#             data.write(str(abstract_llm_input))

#         return prompt

#     def prompt_for_conclusion(self, search_result):
#         # breakpoint()
#         conclusions =  search_result.get("default_results", {}).get("Conclusion", {})

#         if not conclusions:  
#             conclusions = search_result["user_based_search"].items()

#         conclusion_formatted_data = {"Conclusion": conclusions}

#         # Convert to JSON string
#         conclusion_llm_input = json.dumps(conclusion_formatted_data, indent=4)

#         prompt = f'''
#         I am providing a JSON containing conclusions from multiple academic papers, along with their similarity scores. Your task is to generate a concise, well-structured, and academically written summarized conclusion that effectively synthesizes the key findings, implications, and future directions of the given papers.

#         Instructions:
#         - The summary should be formal and academic in tone.
#         - Clearly state the main findings and their significance.
#         - Highlight common conclusions while avoiding redundancy.
#         - Discuss practical implications, limitations, and possible future research directions.
#         - Ensure coherence, logical flow, and clarity in presenting the summary.
        
#         Input: {conclusion_llm_input}

#         Note:  Do not include text like I understand or here is your summary and Do not mension heading at start.

#         Output Format:
#         Provide a well-structured and academically written conclusion that encapsulates the key takeaways and potential future directions from the provided conclusions.        

#         '''
        
#         with open('./extracted/conclusion.txt','w',encoding='utf-8') as data:
#             data.write(str(conclusion_llm_input))

#         return prompt
    
#     def prompt_for_reference(self, search_result):
#         references =  search_result.get("default_results", {}).get("References", {})

#         if not references:  
#             references = search_result["user_based_search"].items()

#         reference_formatted_data = {"References": references}

#         # Convert to JSON string
#         reference_llm_input = json.dumps(dict(reference_formatted_data), indent=4)

#         prompt = f'''
#         I am providing extracted text containing references from multiple academic papers. Your task is to provide extract, organize, deduplicate, and format these references into a properly structured academic reference section output, You can also remove some irrilated papers from it.

#         Example Output:
#         [1]   Zeiler, M. D. and Fergus, “Visualizing and understanding convolutional networks”. European Conference on Computer Vision, vol 8689. Springer, Cham, pp. 818-833, 2014. 
#         [2]   Yann LeCun, Yoshua Bengio, Geoffery  Hinton,  “Deep  Learning”, Nature, Volume 521, pp. 436-444, Macmillan Publishers, May 2015.

#         Input:
#         {reference_llm_input}

#         Note:  Do not include text like I understand or here is your summary and Do not mension heading at start, Name of the Paper should be in double quotes "Visualizing and understanding convolutional networks".

#         Output:
#         Provide a output which is well-structured, serialized with [N] where N is a number, deduplicated, and properly formatted reference list in a consistent academic citation style. Do not include any additional text or explanations—only the final formatted references.
#         '''
        
#         with open('./extracted/reference.txt','w',encoding='utf-8') as data:
#             data.write(str(reference_llm_input))

#         return prompt
    
#     def prompt_for_methodology(self, search_result):
#         methodologys =  search_result.get("default_results", {}).get("Methodology", {})
#         if not methodologys:  
#             methodologys = search_result["user_based_search"].items()

#         methodology_formatted_data = {"Methodology": methodologys}

#         try:
#             methodology_llm_input = json.dumps(methodology_formatted_data, indent=4)
#         except TypeError as e:
#             print("JSON Serialization Error:", e)
#             print("Data that caused the issue:", methodology_formatted_data)
#             return None

#         prompt = f'''

#         I am providing a JSON containing methodologies from multiple academic papers, along with their similarity scores. Your task is to generate a concise, well-structured, and academically written summarized methodology that accurately captures the research approach, experimental setup, and techniques used in the given papers.

#         Instructions:
#         - The summary should be formal and academic in tone.
#         - Clearly describe the research design, data sources, techniques, and procedures used.
#         - Retain key methodological details while eliminating redundancy.
#         - Ensure the summary is coherent, logically structured, and technically precise.
#         - If multiple methodologies are provided, highlight common approaches and differences, if relevant.
        
#         Input:{methodology_llm_input}

#         Note:  Do not include text like I understand or here is your summary and Do not mension heading at start.
        
#         Output Format:
#         Provide a well-structured and academically written methodology summary that effectively synthesizes the approaches used in the given papers.

#         '''
        
#         with open('./extracted/methodology.txt','w',encoding='utf-8') as data:
#             data.write(str(methodology_llm_input))

#         return prompt
    
#     def prompt_for_result(self, search_result):
#         results = search_result.get("default_results", {}).get("Results") 

#         if not results:  
#             results = search_result["user_based_search"].items()

#         result_formatted_data = {"Results": results}

#         # Convert to JSON string
#         result_llm_input = json.dumps(result_formatted_data, indent=4)

#         prompt = f'''
#         I am providing a JSON containing results from multiple academic papers, along with their similarity scores. Your task is to generate a concise, well-structured, and academically written summarized results section that effectively presents the key findings, trends, and insights from the given papers.

#         Instructions:
#         - The summary should be formal and academic in tone.
#         - Clearly highlight the main findings, patterns, and statistical outcomes from the provided texts.
#         - Retain key quantitative and qualitative insights while avoiding redundancy.
#         - Ensure the summary is coherent, logically structured, and concise.
#         - If applicable, mention comparisons, significant improvements, or deviations observed in the results.

#         Input: {result_llm_input}

#         Note:  Do not include text like I understand or here is your summary and Do not mension heading at start.


#         Output Format:
#         Provide a well-structured and academically written results summary that effectively synthesizes the key outcomes from the given papers.
#         '''
        
#         with open('./extracted/results.txt','w',encoding='utf-8') as data:
#             data.write(str(result_llm_input))

#         return prompt
    
#     def prompt_for_lit_review(self, references):

#         prompt=f'''

#         You are an AI model designed to generate a well-structured Literature Review section in IEEE format based on given references. Your task is to synthesize the key findings, methodologies, and contributions of the provided papers while maintaining an academic writing style.

#         Instructions:
#         - Summarize Key Findings - Extract and summarize relevant insights from each reference, ensuring that similar studies are grouped logically.
#         - Cite Properly - Use IEEE citation format, e.g., "Handwriting digit recognition has been extensively studied using neural networks [1]."
#         - Maintain Logical Flow - Organize the literature review into a coherent structure, categorizing related studies.
#         - Use Formal Language - Ensure the text aligns with academic writing standards and maintains objectivity.
#         - Avoid Direct Copying - Rewrite and paraphrase information in a scholarly manner.
#         Example Input:
#         [1] Abu Ghosh, M.M., & Maghari, A.Y. (2017). A Comparative Study on Handwriting Digit Recognition Using Neural Networks. *IEEE*.  
#         [2] Alizadeh, S., & Fazel, A. (2017). Convolutional Neural Networks for Facial Expression Recognition. *Computer Vision and Pattern Recognition*. Cornell University Library.
#         Expected Output:
        
#         Handwriting digit recognition has been widely explored using neural networks. Abu Ghosh and Maghari [1] conducted a comparative analysis of different neural network architectures, demonstrating that convolutional neural networks (CNNs) outperform traditional multilayer perceptron models in terms of accuracy and robustness. Their study highlights the importance of feature extraction and layer depth in achieving high classification performance.

#         Similarly, CNNs have also been applied to facial expression recognition. Alizadeh and Fazel [2] proposed a deep learning approach that utilizes convolutional layers to automatically extract features from facial images, achieving state-of-the-art accuracy. Their work underscores the effectiveness of deep networks in recognizing complex patterns in visual data.

#         By leveraging CNNs, both studies demonstrate the adaptability of deep learning in computer vision applications, reinforcing the need for optimized architectures tailored to specific recognition tasks.

#         Note:  Do not include text like I understand or here is your summary and Do not mension heading at start.
#                Do not mention multiple i.e. more then one reference together eg [3, 4] or [1, 5 , 9] is not allowed.

#         INPUT:
#         {references}
#         '''
        
#         with open('./extracted/lit_review.txt','w',encoding='utf-8') as data:
#             data.write(str(prompt))

#         return prompt
    
#     def prompt_for_caption(self, caption): 
#         prompt = f'''
#             You are an expert in academic writing. Your task is to generate a clear, informative, and concise figure caption for a research paper. 

#             **Context:** The following text describes a figure from the paper. Extract the key information and create a caption that highlights the most relevant aspects.

#             **Figure Description:** 
#             "{caption}"

#             **Instructions:**
#             - Summarize the key idea conveyed by the figure.
#             - Ensure the caption is clear, precise, and relevant to the topic.
#             - Use formal academic language.
#             - Keep it concise (one or two sentences).

#             **Output Format:** 
#             A standalone caption that accurately represents the figure.

#             **Example Output:** 
#             "Figure X: Visualization of [main concept], demonstrating [key insight] as observed in [data or context]."
#         '''
#         with open('./extracted/caption_image_prompt.txt', 'w', encoding='utf-8') as data:
#             data.write(str(prompt))

#         return prompt

















# import json

# def make_serializable(obj):
#     """Recursively convert objects like dict_items to standard JSON-serializable types."""
#     if isinstance(obj, dict):
#         return {k: make_serializable(v) for k, v in obj.items()}
#     elif isinstance(obj, (list, tuple)):
#         return [make_serializable(i) for i in obj]
#     elif hasattr(obj, "items"):  # covers dict_items and similar
#         return {k: make_serializable(v) for k, v in obj.items()}
#     else:
#         return obj


# class LLMPrompt:
#     def __init__(self):
#         self.user_results = []

#     def prompt_for_user_based_search(self, search_result):
#         for key, value in search_result["user_based_search"].items():
#             for entry in value:
#                 self.user_results.append(entry)

#         user_query_llm_input = json.dumps(self.user_results, indent=4)

#         prompt = f'''
# I am providing a JSON containing text excerpts that match a user's query with a similarity score of 0.85 or higher. Your task is to generate concise, well-structured, and contextually relevant headings, sub-headings, and summaries based on this content.

# ### Input:
# {user_query_llm_input}

# ### Output Format:
# - Use Markdown headings (##) and sub-headings (###)
# - Ensure summaries are clear, concise, and relevant
#         '''

#         with open('./extracted/userbased.txt','w',encoding='utf-8') as data:
#             data.write(prompt)

#         return prompt

#     def prompt_for_intro(self, search_result):
#         intros = search_result.get("default_results", {}).get("Introduction", {})
#         if not intros:
#             intros = list(search_result["user_based_search"].items())

#         intro_formatted_data = {"Introduction": intros}
#         serializable_data = make_serializable(intro_formatted_data)
#         intro_llm_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# I am providing a JSON containing introductions from multiple academic papers. Your task is to generate a concise, academically written summarized introduction.

# Input: {intro_llm_input}
# Output Format: Well-structured introduction summarizing key elements.
#         '''

#         with open('./extracted/introduction.txt','w',encoding='utf-8') as data:
#             data.write(intro_llm_input)

#         return prompt

#     def prompt_for_abstract(self, search_result):
#         abstracts = search_result.get("default_results", {}).get("Abstract", {})
#         if not abstracts:
#             abstracts = list(search_result["user_based_search"].items())

#         abstract_formatted_data = {"Abstract": abstracts}
#         serializable_data = make_serializable(abstract_formatted_data)
#         abstract_llm_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# I am providing a JSON containing abstracts from multiple academic papers. Your task is to generate a concise, academically written summarized abstract.

# Input: {abstract_llm_input}
# Output Format: Single, clear, academic abstract.
#         '''

#         with open('./extracted/abstract.txt','w',encoding='utf-8') as data:
#             data.write(abstract_llm_input)

#         return prompt

#     def prompt_for_conclusion(self, search_result):
#         conclusions = search_result.get("default_results", {}).get("Conclusion", {})
#         if not conclusions:
#             conclusions = list(search_result["user_based_search"].items())

#         conclusion_formatted_data = {"Conclusion": conclusions}
#         serializable_data = make_serializable(conclusion_formatted_data)
#         conclusion_llm_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# I am providing a JSON containing conclusions from multiple academic papers. Your task is to generate a concise, academically written summarized conclusion.

# Input: {conclusion_llm_input}
# Output Format: Well-structured conclusion summarizing key takeaways.
#         '''

#         with open('./extracted/conclusion.txt','w',encoding='utf-8') as data:
#             data.write(conclusion_llm_input)

#         return prompt

#     def prompt_for_reference(self, search_result):
#         references = search_result.get("default_results", {}).get("References", {})
#         if not references:
#             references = list(search_result["user_based_search"].items())

#         reference_formatted_data = {"References": references}
#         serializable_data = make_serializable(reference_formatted_data)
#         reference_llm_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# I am providing extracted references from multiple academic papers. Your task is to deduplicate, organize, and format these references academically.

# Input: {reference_llm_input}
# Output Format: Properly formatted reference list.
#         '''

#         with open('./extracted/reference.txt','w',encoding='utf-8') as data:
#             data.write(reference_llm_input)

#         return prompt

#     def prompt_for_methodology(self, search_result):
#         methodologies = search_result.get("default_results", {}).get("Methodology", {})
#         if not methodologies:
#             methodologies = list(search_result["user_based_search"].items())

#         methodology_formatted_data = {"Methodology": methodologies}
#         serializable_data = make_serializable(methodology_formatted_data)
#         methodology_llm_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# I am providing a JSON containing methodologies from multiple academic papers. Your task is to generate a concise, academically written summarized methodology.

# Input: {methodology_llm_input}
# Output Format: Well-structured methodology summary.
#         '''

#         with open('./extracted/methodology.txt','w',encoding='utf-8') as data:
#             data.write(methodology_llm_input)

#         return prompt

#     def prompt_for_result(self, search_result):
#         results = search_result.get("default_results", {}).get("Results", {})
#         if not results:
#             results = list(search_result["user_based_search"].items())

#         result_formatted_data = {"Results": results}
#         serializable_data = make_serializable(result_formatted_data)
#         result_llm_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# I am providing a JSON containing results from multiple academic papers. Your task is to generate a concise, academically written summarized results section.

# Input: {result_llm_input}
# Output Format: Well-structured results summary.
#         '''

#         with open('./extracted/results.txt','w',encoding='utf-8') as data:
#             data.write(result_llm_input)

#         return prompt

#     def prompt_for_lit_review(self, references):
#         serializable_data = make_serializable(references)
#         references_input = json.dumps(serializable_data, indent=4)

#         prompt = f'''
# You are an AI model designed to generate a literature review based on provided references.

# Input: {references_input}
# Output Format: Well-structured literature review in IEEE style.
#         '''

#         with open('./extracted/lit_review.txt','w',encoding='utf-8') as data:
#             data.write(references_input)

#         return prompt

#     def prompt_for_caption(self, caption):
#         prompt = f'''
# You are an expert in academic writing. Generate a clear, concise figure caption.

# Figure Description: "{caption}"

# Output Format: One or two sentence caption.
#         '''

#         with open('./extracted/caption_image_prompt.txt','w',encoding='utf-8') as data:
#             data.write(prompt)

#         return prompt














# llm_prompt.py
# import json

# def make_serializable(obj):
#     if isinstance(obj, dict):
#         return {k: make_serializable(v) for k, v in obj.items()}
#     elif isinstance(obj, (list, tuple)):
#         return [make_serializable(i) for i in obj]
#     elif hasattr(obj, "items"):
#         return {k: make_serializable(v) for k, v in obj.items()}
#     else:
#         return obj


# class LLMPrompt:
#     def __init__(self):
#         pass

#     def prompt_for_user_based_search(self, search_result):
#         user_query = search_result.get("query", "the topic")
#         results = []
#         for coll, hits in search_result["user_based_search"].items():
#             for hit in hits:
#                 hit["source_collection"] = coll
#                 results.append(hit)

#         input_json = json.dumps(make_serializable(results), indent=2, ensure_ascii=False)

#         prompt = f'''You are an expert academic researcher writing a high-quality survey paper section titled:

# "{user_query.capitalize()}"

# Below are the most relevant excerpts (similarity ≥ 0.80) from multiple research papers on this topic.

# Your task:
# - Create a detailed, well-structured technical section with meaningful headings (##) and subheadings (###)
# - Synthesize insights across papers — do not list them separately
# - Use formal academic English
# - Include inline citations using [1], [2], ... format
# - Use $...$ for inline math, $$...$$ for display math
# - Remove redundancy, highlight differences and trends
# - Number subsections logically (e.g., 4.1, 4.2)

# Input excerpts (with source paper and similarity score):
# {input_json}

# Output only the Markdown content for this section. Start directly with the first ## heading.
# '''
#         with open('./extracted/userbased.txt', 'w', encoding='utf-8') as f:
#             f.write(prompt)
#         return prompt

#     def prompt_for_abstract(self, search_result):
#         abstracts = search_result.get("default_results", {}).get("Abstract", {}) or search_result.get("default_results", {}).get("Introduction", {})
#         data = make_serializable({"Abstracts": list(abstracts.values())})
#         input_json = json.dumps(data, indent=2, ensure_ascii=False)

#         prompt = f'''Write a concise, publication-quality abstract (150–250 words) for a survey paper based on the following abstracts from related papers.

# Requirements:
# - Highlight the importance of the field
# - Summarize key approaches and trends
# - State the goal of this survey
# - End with contributions or scope

# Input:
# {input_json}

# Output only the abstract text. No title, no "Here is the abstract".
# '''
#         return prompt

#     def prompt_for_intro(self, search_result):
#         intros = search_result.get("default_results", {}).get("Introduction", {}) or search_result.get("default_results", {}).get("Background", {})
#         data = make_serializable({"Introductions": list(intros.values())})
#         input_json = json.dumps(data, indent=2, ensure_ascii=False)

#         prompt = f'''Write a compelling 3–4 paragraph introduction for a survey paper.

# Include:
# - Motivation and real-world importance
# - Evolution of the field
# - Key challenges and open problems
# - What this survey covers and its contributions

# Use academic tone. Cite where appropriate with [1], [2].

# Input:
# {input_json}

# Output only the introduction text.
# '''
#         return prompt

#     def prompt_for_lit_review(self, search_result):
#         # Use Related Work, Literature Review, Background, Introduction
#         sources = {}
#         for key in ["Related Work", "Literature Review", "Background", "Introduction"]:
#             if key in search_result.get("default_results", {}):
#                 sources.update(search_result["default_results"][key])
#         if not sources:
#             sources = search_result.get("default_results", {}).get("Introduction", {})

#         data = make_serializable({"Literature": list(sources.values())})
#         input_json = json.dumps(data, indent=2, ensure_ascii=False)

#         prompt = f'''Write a comprehensive "Related Work" section (800–1200 words) that:

# - Groups prior work into 3–5 coherent themes or approaches
# - Compares and contrasts methods chronologically or thematically
# - Highlights strengths, limitations, and gaps
# - Uses smooth transitions
# - Cites extensively with [1], [2], etc.

# Input excerpts:
# {input_json}

# Output only the Markdown content starting with ## Related Work
# '''
#         return prompt

#     def prompt_for_methodology(self, search_result):
#         methods = search_result.get("default_results", {}).get("Methodology", {}) or search_result.get("default_results", {}).get("Methods", {})
#         data = make_serializable({"Methodology": list(methods.values())})
#         input_json = json.dumps(data, indent=2, ensure_ascii=False)

#         prompt = f'''Write a "Methodology Overview" section summarizing common techniques.

# Group into categories (e.g., data augmentation, loss functions, architectures).
# Explain core ideas and cite [1], [2].

# Input:
# {input_json}

# Output only the section content.
# '''
#         return prompt

#     def prompt_for_result(self, search_result):
#         results = search_result.get("default_results", {}).get("Results", {}) or search_result.get("default_results", {}).get("Experiments", {})
#         data = make_serializable({"Results": list(results.values())})
#         input_json = json.dumps(data, indent=2, ensure_ascii=False)

#         prompt = f'''Write a "Performance Comparison" section.

# Include:
# - Common datasets and metrics
# - State-of-the-art results
# - Trends (e.g., larger models = better performance)
# - Use tables if helpful (Markdown tables are fine)

# Input:
# {input_json}

# Output only the section.
# '''
#         return prompt

#     def prompt_for_conclusion(self, search_result):
#         conclusions = search_result.get("default_results", {}).get("Conclusion", {}) or search_result.get("default_results", {}).get("Discussion", {})
#         data = make_serializable({"Conclusions": list(conclusions.values())})
#         input_json = json.dumps(data, indent=2, ensure_ascii=False)

#         prompt = f'''Write a strong conclusion that:
# - Summarizes key findings
# - Discusses broader impact
# - Suggests 3–4 future directions
# - Ends memorably

# Input:
# {input_json}

# Output only the conclusion.
# '''
#         return prompt

# #     def prompt_for_reference(self, search_result):
# #         refs = search_result.get("default_results", {}).get("References", {})
# #         text = "\n".join([item.get("text", "") for item in refs.values()])
        
# #         prompt = f'''Extract, deduplicate, and format all references in clean IEEE style.

# # Rules:
# # - Deduplicate by title (keep most complete)
# # - Format: [1] Author1, Author2, et al., "Title," Journal/Conference, vol, no, pp, year.
# # - If arXiv: [1] Author et al., "Title," arXiv:xxxx.xxxxx, 2024.

# # Input text:
# # {text}

# # Output only the formatted list, one per line, starting with [1], [2], etc.
# # '''
# #         return prompt

    
#         def prompt_for_reference(self, search_result):
#         # Extract all reference text from default_results["References"]
#             refs = search_result.get("default_results", {}).get("References", {})
#             all_ref_texts = []

#             for collection_name, hits in refs.items():
#                 for hit in hits:  # hits is a list
#                     text = hit.get("text", "")
#                     if text.strip():
#                         all_ref_texts.append(text.strip())

#             raw_text = "\n".join(all_ref_texts) if all_ref_texts else "No references found."

#             prompt = f'''You are an expert academic librarian. Extract, clean, deduplicate, and reformat all references below into proper IEEE style.

#     Rules:
#     - Remove page headers, footers, "References" title
#     - Deduplicate by title (keep the most complete entry)
#     - Format exactly like:
#     [1] A. Author et al., "Paper Title," Journal Name, vol. X, no. Y, pp. 123-456, 2024.
#     [2] B. Author and C. Coauthor, "Another Title," in Proc. ConfName, 2023, doi:10.123/abc.
#     [3] Name et al., "Title," arXiv:2400.12345 [cs.CV], 2024.

#     Input references (raw extracted text):
#     {raw_text}

#     Output ONLY the clean numbered list starting with [1], [2], etc. No extra text.
#     '''
#             with open('./extracted/reference_prompt.txt', 'w', encoding='utf-8') as f:
#                 f.write(prompt)
#             return prompt

#     def prompt_for_caption(self, caption_text, image_path):
#         prompt = f'''Write a clear, concise, and informative figure caption (1–2 sentences) for a survey paper.

# Image context: {caption_text}

# Make it academic and descriptive.

# Example: "Overview of the self-supervised learning pipeline, showing pretext task generation, encoder training, and downstream evaluation."

# Output only the caption text.
# '''
#         return prompt












# llm_prompt.py
import json

def make_serializable(obj):
    if isinstance(obj, dict):
        return {k: make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [make_serializable(i) for i in obj]
    elif hasattr(obj, "items"):
        return {k: make_serializable(v) for k, v in obj.items()}
    else:
        return obj


class LLMPrompt:
    def __init__(self):
        pass

    def prompt_for_user_based_search(self, search_result):
        user_query = search_result.get("query", "the topic")
        results = []
        for coll, hits in search_result["user_based_search"].items():
            for hit in hits:
                hit = hit.copy()
                hit["source_collection"] = coll
                results.append(hit)

        input_json = json.dumps(make_serializable(results), indent=2, ensure_ascii=False)

        prompt = f'''You are an expert academic researcher writing a high-quality survey paper section titled:

"{user_query.capitalize()}"

Below are the most relevant excerpts from multiple research papers.

Your task:
- Create a detailed, well-structured technical section with meaningful headings (##) and subheadings (###)
- Synthesize insights — do not list papers
- Use formal academic English
- Include inline citations using [1], [2], ...
- Use $...$ for inline math, $$...$$ for display math
- Remove redundancy, highlight trends

Input excerpts:
{input_json}

Output only the Markdown content. Start directly with the first ## heading.
'''
        return prompt

    def prompt_for_abstract(self, search_result):
        abstracts = search_result.get("default_results", {}).get("Abstract", {}) or {}
        data = make_serializable({"Abstracts": [h["text"] for coll in abstracts.values() for h in coll]})
        input_json = json.dumps(data, indent=2, ensure_ascii=False)

        prompt = f'''Write a concise, publication-quality abstract (150–250 words) for a survey paper.

Input:
{input_json}

Output only the abstract text.
'''
        return prompt

    def prompt_for_intro(self, search_result):
        intros = search_result.get("default_results", {}).get("Introduction", {}) or {}
        data = make_serializable({"Introductions": [h["text"] for coll in intros.values() for h in coll]})
        input_json = json.dumps(data, indent=2, ensure_ascii=False)

        prompt = f'''Write a compelling 3–4 paragraph introduction for a survey paper.

Include motivation, challenges, and what this survey covers.

Input:
{input_json}

Output only the introduction text.
'''
        return prompt

    def prompt_for_lit_review(self, search_result):
        sources = {}
        for key in ["Related Work", "Literature Review", "Background", "Introduction"]:
            sources.update(search_result.get("default_results", {}).get(key, {}))
        data = make_serializable({"Literature": [h["text"] for coll in sources.values() for h in coll]})
        input_json = json.dumps(data, indent=2, ensure_ascii=False)

        prompt = f'''Write a comprehensive "Related Work" section (800–1200 words) that groups prior work into themes, compares methods, and identifies gaps.

Input:
{input_json}

Output only the Markdown content starting with ## Related Work
'''
        return prompt

    def prompt_for_methodology(self, search_result):
        methods = search_result.get("default_results", {}).get("Methodology", {}) or {}
        data = make_serializable({"Methodology": [h["text"] for coll in methods.values() for h in coll]})
        input_json = json.dumps(data, indent=2, ensure_ascii=False)

        prompt = f'''Write a "Methodology Overview" section summarizing common techniques.

Input:
{input_json}

Output only the section content.
'''
        return prompt

    def prompt_for_result(self, search_result):
        results = search_result.get("default_results", {}).get("Results", {}) or {}
        data = make_serializable({"Results": [h["text"] for coll in results.values() for h in coll]})
        input_json = json.dumps(data, indent=2, ensure_ascii=False)

        prompt = f'''Write a "Performance Comparison" section with key datasets, metrics, and trends.

Input:
{input_json}

Output only the section.
'''
        return prompt

    def prompt_for_conclusion(self, search_result):
        conclusions = search_result.get("default_results", {}).get("Conclusion", {}) or {}
        data = make_serializable({"Conclusions": [h["text"] for coll in conclusions.values() for h in coll]})
        input_json = json.dumps(data, indent=2, ensure_ascii=False)

        prompt = f'''Write a strong conclusion summarizing findings and suggesting future work.

Input:
{input_json}

Output only the conclusion.
'''
        return prompt

    def prompt_for_reference(self, search_result):
        refs = search_result.get("default_results", {}).get("References", {})
        all_ref_texts = []
        for collection_name, hits in refs.items():
            for hit in hits:
                text = hit.get("text", "")
                if text.strip():
                    all_ref_texts.append(text.strip())

        raw_text = "\n".join(all_ref_texts) if all_ref_texts else "No references found."

        prompt = f'''You are an expert academic librarian. Extract, clean, deduplicate, and reformat all references below into proper IEEE style.

Rules:
- Remove headers/footers
- Deduplicate by title
- Format: [1] Author et al., "Title," Journal, vol. X, no. Y, pp. 123-456, 2024.

Input:
{raw_text}

Output ONLY the clean numbered list starting with [1], [2], etc.
'''
        return prompt

    def prompt_for_caption(self, caption_text, image_path):
        prompt = f'''Write a clear, concise, academic figure caption (1–2 sentences).

Context: {caption_text}

Output only the caption.
'''
        return prompt