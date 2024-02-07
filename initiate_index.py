import os

from llama_index import StorageContext, load_index_from_storage, SimpleDirectoryReader, VectorStoreIndex


def initiate_index():  # Have done fully according to the documentation and the tutorials that I was able to find. I think I'm even able to explain how it is actually working
    if os.path.exists("./storage"):
        storage_context = StorageContext.from_defaults(persist_dir='./storage')  # using it to read the data from the storage for further use
        index = load_index_from_storage(storage_context=storage_context)  # creating index based on storage files
    else:
        documents = SimpleDirectoryReader(f"data").load_data()  # providing the name of the folder and it returns the list of content inside the folder
        index = VectorStoreIndex.from_documents(documents)  # here we're deviding documents into the chunks in vector store and thus creating the instance of the index
        index.storage_context.persist()  # creating the storage with json file for a further usage
    return index