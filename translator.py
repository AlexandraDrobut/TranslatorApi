from google.cloud import translate_v2 as translate


caption_file_path="/home/alexandra/generate_captions/translator_api/descriptions.txt"
trans_file_path="/home/alexandra/generate_captions/translator_api/translations.txt"

def main():
	translate_client = translate.Client()
	caption_file = open(caption_file_path, "r")
	translated_lines= []
	caption_lines = caption_file.readlines()
	caption_file.close()

	lines_len = len(caption_lines)
	for i in range(lines_len):
		caption = caption_lines[i].split(" ", maxsplit=1)[1]
		result = translate_client.translate(caption, target_language='ro', model="nmt")
		translation = result['translatedText']
		translation = translation + '\n'
		translated_lines.append(translation)

	translat_file = open(trans_file_path, "w+")
	translat_file.writelines(translated_lines)
	translat_file.close()

if __name__ == "__main__":
	main()


