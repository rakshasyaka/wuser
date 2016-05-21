$all_upd_groups = Get-CMSoftwareUpdateGroup
$all_auto_rules = Get-CMSoftwareUpdateAutoDeploymentRule
$auto_rules_names = Get-Content E:\scripts\wuser\auto_rules.txt
foreach($rule_name in $auto_rules_names){
    if($rule_name -match "_"){
        $rule_path = $rule_name.Replace("_", "-")
    }
    else{$rule_path = $rule_name}
    $path = "E:\scripts\wuser\" + $rule_path
    $rule_id = $all_auto_rules | where {$_.name -eq $rule_name}
    $rule_id = $rule_id.AutoDeploymentID
    $s_upd_group = $all_upd_groups | where {$_.AssociatedAutoRuleID -eq $rule_id}
    #$s_upd_group.numberOfUpdates | Out-File $path -Append
    #"=======" | Out-File $path -Append
    #$s_upd_group.updates | Out-File $path -Append
    Write-Host $rule_name -ForegroundColor Red
    Write-Host $rule_path -ForegroundColor Blue
    Write-Host $path
}
