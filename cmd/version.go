package cmd

import (
	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

// versionCmd represents the version command
var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "Show the version of Moldy CLI",
	Long:  `Show the version of Moldy CLI`,
	Run: func(cmd *cobra.Command, args []string) {
		color.Cyan("Moldy CLI Version 0.5 BETA")
	},
}

func init() {
	rootCmd.AddCommand(versionCmd)
}
