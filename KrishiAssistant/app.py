from pipeline.rag_chatbot import create_rag_chain
from pipeline.fallback import fallback_answer
from utils.translator import detect_language, translate_to_english, translate_from_english
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def main():
    rag, _ = create_rag_chain()

    print(" AgriChatBot is ready! Ask your agriculture-related questions.\n")
    while True:
        query = input("Query: ")
        if query.lower() in ["exit", "quit"]:
            break
        # DDetect & Translate
        source_lang = detect_language(query)
        query_en = translate_to_english(query) if source_lang != "en" else query

        try:
            response = rag.invoke({"query": query_en})
            result = response.get("result", "").strip()
            sources = response.get("source_documents", [])


            #  Fallback only if result is missing or weak
            if not sources or not result or "i don't know" in result.lower():
                print("No relevant result found. Falling back to Mistral...")
                answer_en = fallback_answer(query_en)
            else:
                answer_en = result

        except Exception as e:
            #print(e)
            answer_en = fallback_answer(query_en)

        final_answer = translate_from_english(answer_en, source_lang) if source_lang != "en" else answer_en
        print("Eng-Reply:",answer_en.strip())
        print("Query-Lang-Reply:", final_answer)

if __name__ == "__main__":
    main()

