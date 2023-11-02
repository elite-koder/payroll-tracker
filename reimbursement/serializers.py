from rest_framework import serializers
from reimbursement.models import ExpenseClaim, ExpenseProof
from django.db import transaction

class ExpenseProofCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseProof
        fields = ["file"]
        

class ExpenseClaimCreateSerializer(serializers.ModelSerializer):
    proofs = ExpenseProofCreateSerializer(many=True)
    class Meta:
        model = ExpenseClaim
        fields = ["id", "employee", "amount", "desc", "proofs"]

    def create(self, validated_data):
        proofs = validated_data.pop("proofs")
        with transaction.atomic():
            expense_claim = super().create(validated_data)
            expense_claim.proofs.add(*ExpenseProof.objects.bulk_create([ExpenseProof(file=proof["file"]) for proof in proofs]))
            return expense_claim

class ExpenseClaimReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseClaim
        fields = ["id", "status"]