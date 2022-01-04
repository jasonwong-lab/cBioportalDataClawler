from bravado.client import SwaggerClient
import csv


cbioportal = SwaggerClient.from_url('https://www.cbioportal.org/api/api-docs',
                                    config={"validate_requests":False, "validate_responses":False,
                                            "validate_swagger_spec": False})

mutations = cbioportal.Mutations.getMutationsInMolecularProfileBySampleListIdUsingGET(
    molecularProfileId='pan_origimed_2020_mutations',
    sampleListId='pan_origimed_2020_all',
    projection='DETAILED'
).result()

cna = cbioportal.Discrete_Copy_Number_Alterations.getDiscreteCopyNumbersInMolecularProfileUsingGET(
    molecularProfileId='pan_origimed_2020_cna',
    sampleListId='pan_origimed_2020_all'
).result()

structual_variants = cbioportal.Structural_Variants.fetchStructuralVariantsUsingPOST(
    structuralVariantFilter={
        'molecularProfileIds':['pan_origimed_2020_fusion']
    }
).result()


def get_csv_by_list(data):
    attributes = dir(data[0])  # Return a list of valid attributes for the object data[0].
    values = []
    temp = []
    for i in range(len(data)):
        for j in range(len(attributes)):
            att_value = getattr(data[i], attributes[j])  # Return the value of the attribute attributes[j] of object data[i]
                                                         # getattr(x, 'foobar') is equivalent to x.foobar.
            temp.append(att_value)
        values.append(temp)
        temp = []

    values.insert(0, attributes)  # Insert the 1d list "attributes" into the 2d list "values" at its position 0,
                                  # so that the "values" can include the .
    return values


def save_csv(two_d_list, savepath):
    with open(savepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(two_d_list)


cna_values = get_csv_by_list(data=cna)
mutations_values = get_csv_by_list(data=mutations)
structual_variants_values = get_csv_by_list(data=structual_variants)

save_csv(cna_values, "cna.csv")
save_csv(mutations_values, "mutations.csv")
save_csv(structual_variants_values, "structual_variants.csv")




# To verify the download results, we can count and compare the number of genes.

#Based on https://www.cbioportal.org/study/summary?id=pan_origimed_2020, the 10 most common genes should be:
# {'TP53': 6246, 'LRP1B': 1904, 'APC': 1822, 'KRAS': 1731, 'EGFR': 1326, 'KMT2D': 1209, 'FAT3': 1177,'ARID1A': 1134, 'PIK3CA': 1090, 'SPTA1': 1068}

# mutation_counts = Counter([m.gene.hugoGeneSymbol for m in mutations])
# print(mutation_counts.most_common(10))

# structual_variants_counts = Counter([m.site1HugoSymbol for m in structual_variants])
# print(structual_variants_counts.most_common(10))
